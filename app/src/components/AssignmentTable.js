import React from "react";

const AssignmentTable = (props) => (
  <table>
    <thead>
      <tr>
        <th>assignmentID</th>
        <th>instructorID</th>
        <th>courseID</th>
      </tr>
    </thead>
    <tbody>
      {props.assignments.length > 0 ? (
        props.assignments.map((assignment) => (
          <tr key={assignment.assignmentID}>
            <td>{assignment.assignmentID}</td>
            <td>{assignment.instructorID}</td>
            <td>{assignment.courseID}</td>
            <td>
              <button className="button muted-button">Edit</button>
              <button className="button muted-button">Delete</button>
            </td>
          </tr>
        ))
      ) : (
        <tr>
          <td colSpan={3}>No assignments</td>
        </tr>
      )}
    </tbody>
  </table>
);

export default AssignmentTable;
