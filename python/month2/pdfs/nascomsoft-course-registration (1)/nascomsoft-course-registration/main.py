"""FastAPI endpoints and HTML forms for the Nascomsoft classroom project."""

from urllib.parse import urlencode

from fastapi import Body, FastAPI, Form, HTTPException, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from data_store import (
    COURSES,
    add_enrollment,
    find_course,
    find_enrollment,
    list_enrollments,
    remove_enrollment,
    update_enrollment,
)

app = FastAPI(title="Nascomsoft Course Registration API", version="1.0.0")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/courses")
def get_courses():
    return COURSES


@app.get("/courses/{course_id}")
def get_course(course_id: int):
    course = find_course(course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found.")
    return course


@app.get("/enrollments")
def get_enrollments(course_id: int | None = None):
    if course_id is not None and find_course(course_id) is None:
        raise HTTPException(status_code=404, detail="Course not found.")
    return list_enrollments(course_id)


@app.get("/enrollments/{enrollment_id}")
def get_enrollment(enrollment_id: int):
    record = find_enrollment(enrollment_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Enrollment not found.")
    return record


@app.post("/enrollments", status_code=201)
def create_enrollment(payload: dict = Body(...)):
    try:
        return add_enrollment(payload)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error


@app.put("/enrollments/{enrollment_id}")
def replace_enrollment(enrollment_id: int, payload: dict = Body(...)):
    try:
        return update_enrollment(enrollment_id, payload)
    except LookupError as error:
        raise HTTPException(status_code=404, detail=str(error)) from error
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error


@app.delete("/enrollments/{enrollment_id}", status_code=204)
def delete_enrollment(enrollment_id: int):
    try:
        remove_enrollment(enrollment_id)
    except LookupError as error:
        raise HTTPException(status_code=404, detail=str(error)) from error
    return Response(status_code=204)


def redirect_to_dashboard(kind, message):
    query = urlencode({kind: message})
    return RedirectResponse(url=f"/?{query}", status_code=303)


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def dashboard(request: Request, course_id: int | None = None):
    records = list_enrollments(course_id)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "courses": COURSES,
            "enrollments": records,
            "active_course": course_id,
            "success": request.query_params.get("success", ""),
            "error": request.query_params.get("error", ""),
        },
    )


@app.post("/ui/register", include_in_schema=False)
def register_from_form(
    student_name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    course_id: int = Form(...),
):
    data = {
        "student_name": student_name,
        "email": email,
        "phone": phone,
        "course_id": course_id,
    }
    try:
        record = add_enrollment(data)
    except ValueError as error:
        return redirect_to_dashboard("error", str(error))
    return redirect_to_dashboard(
        "success", f"Enrollment #{record['enrollment_id']} created."
    )


@app.post("/ui/enrollments/{enrollment_id}/update", include_in_schema=False)
def update_from_form(
    enrollment_id: int,
    student_name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    course_id: int = Form(...),
):
    data = {
        "student_name": student_name,
        "email": email,
        "phone": phone,
        "course_id": course_id,
    }
    try:
        update_enrollment(enrollment_id, data)
    except (LookupError, ValueError) as error:
        return redirect_to_dashboard("error", str(error))
    return redirect_to_dashboard("success", "Enrollment updated.")


@app.post("/ui/enrollments/{enrollment_id}/delete", include_in_schema=False)
def delete_from_form(enrollment_id: int):
    try:
        remove_enrollment(enrollment_id)
    except LookupError as error:
        return redirect_to_dashboard("error", str(error))
    return redirect_to_dashboard("success", "Enrollment deleted.")
