import React from "react";

const InstructorTable = (props) => (
  <table>
    <thead>
      <tr>
        <th>instructorID</th>
        <th>name</th>
        <th>qualifications</th>
        <th>atUIUC</th>
        <th>semesterAvailable</th>
      </tr>
    </thead>
    <tbody>
      {props.instructors.length > 0 ? (
        props.instructors.map((instructor) => (
          <tr key={instructor.instructorID}>
            <td>{instructor.instructorID}</td>
            <td>{instructor.name}</td>
            <td>{instructor.qualifications}</td>
            <td>{instructor.atUIUC}</td>
            <td>{instructor.semesterAvailable}</td>
            <td>
              <button className="button muted-button">Edit</button>
              <button className="button muted-button">Delete</button>
            </td>
          </tr>
        ))
      ) : (
        <tr>
          <td colSpan={3}>No users</td>
        </tr>
      )}
    </tbody>
  </table>
);

export default InstructorTable;
