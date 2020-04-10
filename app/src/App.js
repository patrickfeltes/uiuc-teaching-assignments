import React, { useState, useEffect } from "react";
import InstructorTable from "./components/InstructorTable";
import AssignmentTable from "./components/AssignmentTable";
import CourseTable from "./components/CourseTable";
import AddInstructorForm from "./components/AddInstructorForm";

const App = () => {
  const [instructors, setInstructors] = useState([]);
  const [courses, setCourses] = useState([]);
  const [assignments, setAssignments] = useState([]);

  //POST Payload to url with payload
  const postPayload = (url, payload) => {
    fetch(url, {
      method: "POST",
      body: payload,
      headers: {
        "Content-Type": "application/json",
      },
    });
  };

  //GET method; only render once (at mounting time)
  useEffect(() => {
    fetch("/instructor").then((response) =>
      response.json().then((data) => setInstructors(data))
    );
  }, []);

  // useEffect(() => {
  //   fetch("/course").then((response) =>
  //     response.json().then((data) => setCourses(data))
  //   );
  // }, []);

  // useEffect(() => {
  //   fetch("/assignment").then((response) =>
  //     response.json().then((data) => setAssignments(data))
  //   );
  // }, []);

  return (
    <div className="container">
      <h1>CS Teaching Assignments Records</h1>
      <div className="flex-row">
        <div className="flex-large">
          <h2>Add instructor</h2>
          <AddInstructorForm postPayload={postPayload} />
        </div>
        <div className="flex-large">
          <h2>View instructors</h2>
          <InstructorTable instructors={instructors} />
        </div>
      </div>

      <div className="flex-row">
        <div className="flex-large">
          <h2>Add assignment</h2>
        </div>
        <div className="flex-large">
          <h2>View assignments</h2>
          <AssignmentTable assignments={[assignments]} />
        </div>
      </div>

      <div className="flex-row">
        <div className="flex-large">
          <h2>Add course</h2>
        </div>
        <div className="flex-large">
          <h2>View courses</h2>
          <CourseTable courses={courses} />
        </div>
      </div>
    </div>
  );
};

export default App;
