import React from "react";
import CRUDTable,
{
  Fields,
  Field,
  CreateForm,
  UpdateForm,
  DeleteForm,
} from 'react-crud-table';
 
const assignmentService = {
  fetchItems: (payload) => {
    return fetch('/assignment').then(response => {
      return response.json();
    });
  },
  create: (assignment) => {
    return fetch('/assignment', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(assignment)
    });
  },
  update: (assignment) => {
    return fetch('/assignment', {
      method: 'PUT',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(assignment)
    });
  },
  delete: (data) => {
    return fetch('/assignment/' + data.assignmentID, {
      method: 'DELETE',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
    });
  },
};
 
const styles = {
  container: { margin: 'auto', width: 'fit-content' },
};
 
const AssignmentTable = () => (
  <div style={styles.container}>
    <CRUDTable
      caption="assignments"
      fetchItems={payload => assignmentService.fetchItems(payload)}
    >
      <Fields>
        <Field
          name="assignmentID"
          label="assignmentTable"
          hideInCreateForm
          hideInUpdateForm
        />
        <Field
          name="courseID"
          label="courseID"
        />
        <Field
          name="instructorID"
          label="instructorID"
        />
        <Field
          name="semester"
          label="semester"
        />
      </Fields>
      <CreateForm
        title="Assignment Creation"
        message="Create a new assignment!"
        trigger="Create assignment"
        onSubmit={task => assignmentService.create(task)}
        submitText="Create"
        validate={(values) => {
          const errors = {};
 
          return errors;
        }}
      />
 
      <UpdateForm
        title="Assignment Update Process"
        message="Update assignment"
        trigger="Update"
        onSubmit={task => assignmentService.update(task)}
        submitText="Update"
        validate={(values) => {
          const errors = {};
 
          return errors;
        }}
      />
 
      <DeleteForm
        title="Assignment Delete Process"
        message="Are you sure you want to delete the assignment?"
        trigger="Delete"
        onSubmit={task => assignmentService.delete(task)}
        submitText="Delete"
        validate={(values) => {
          const errors = {};
          
          return errors;
        }}
      />
    </CRUDTable>
  </div>
);

AssignmentTable.propTypes = {};

export default AssignmentTable;
