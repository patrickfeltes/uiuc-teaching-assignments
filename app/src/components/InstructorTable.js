import React from "react";
import CRUDTable,
{
  Fields,
  Field,
  CreateForm,
  UpdateForm,
  DeleteForm,
} from 'react-crud-table';
 
const BASE_URL = 'https://cs411-server.herokuapp.com';

const instructorService = {
  fetchItems: (payload) => {
    return fetch(BASE_URL + '/instructor').then(response => {
      return response.json();
    });
  },
  create: (instructor) => {
    return fetch(BASE_URL + '/instructor', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(instructor)
    });
  },
  update: (instructor) => {
    return fetch(BASE_URL + '/instructor', {
      method: 'PUT',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(instructor)
    });
  },
  delete: (data) => {
    return fetch(BASE_URL + '/instructor/' + data.instructorID, {
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
 
const InstructorTable = () => (
  <div style={styles.container}>
    <CRUDTable
      caption="Instructors"
      fetchItems={payload => instructorService.fetchItems(payload)}
    >
      <Fields>
        <Field
          name="instructorID"
          label="instructorID"
          hideInCreateForm
          hideInUpdateForm
        />
        <Field
          name="name"
          label="name"
        />
      </Fields>
      <CreateForm
        title="Instructor Creation"
        message="Create a new instructor!"
        trigger="Create Instructor"
        onSubmit={task => instructorService.create(task)}
        submitText="Create"
        validate={(values) => {
          const errors = {};
 
          return errors;
        }}
      />
 
      <UpdateForm
        title="Instructor Update Process"
        message="Update instructor"
        trigger="Update"
        onSubmit={task => instructorService.update(task)}
        submitText="Update"
        validate={(values) => {
          const errors = {};
 
          return errors;
        }}
      />
 
      <DeleteForm
        title="Instructor Delete Process"
        message="Are you sure you want to delete the instructor?"
        trigger="Delete"
        onSubmit={task => instructorService.delete(task)}
        submitText="Delete"
        validate={(values) => {
          const errors = {};
          
          return errors;
        }}
      />
    </CRUDTable>
  </div>
);

InstructorTable.propTypes = {};

export default InstructorTable;
