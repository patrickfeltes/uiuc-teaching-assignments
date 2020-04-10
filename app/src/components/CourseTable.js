import React from "react";

const CourseTable = (props) => (
  <table>
    <thead>
      <tr>
        <th>courseID</th>
        <th>crn</th>
        <th>semester</th>
        <th>description</th>
        <th>numStudents</th>
        <th>dept</th>
        <th>undergrad</th>
        <th>year</th>
        <th>online</th>
        <th>creditHours</th>
      </tr>
    </thead>
    <tbody>
      {props.courses.length > 0 ? (
        props.courses.map((course) => (
          <tr key={course.courseID}>
            <td>{course.courseID}</td>
            <td>{course.crn}</td>
            <td>{course.semester}</td>
            <td>{course.description}</td>
            <td>{course.numStudents}</td>
            <td>{course.dept}</td>
            <td>{course.undergrad}</td>
            <td>{course.year}</td>
            <td>{course.online}</td>
            <td>{course.creditHours}</td>
            <td>
              <button className="button muted-button">Edit</button>
              <button className="button muted-button">Delete</button>
            </td>
          </tr>
        ))
      ) : (
        <tr>
          <td colSpan={3}>No courses</td>
        </tr>
      )}
    </tbody>
  </table>
);

export default CourseTable;
