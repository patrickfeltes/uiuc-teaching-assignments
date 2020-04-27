import React from "react";
import CRUDTable,
{
  Fields,
  Field,
  CreateForm,
  UpdateForm,
  DeleteForm,
} from 'react-crud-table';
 
const courseService = {
  fetchItems: (payload) => {
    return fetch('/course').then(response => {
      return response.json();
    });
  },
  create: (course) => {
    return fetch('/course', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(course)
    });
  },
  update: (course) => {
    return fetch('/course', {
      method: 'PUT',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(course)
    });
  },
  delete: (data) => {
    return fetch('/course/' + data.courseID, {
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
 
const CourseTable = () => (
  <div style={styles.container}>
    <CRUDTable
      caption="course"
      fetchItems={payload => courseService.fetchItems(payload)}
    >
      <Fields>
        <Field
          name="courseID"
          label="courseID"
          hideInCreateForm
          hideInUpdateForm
        />
        <Field
          name="courseNumber"
          label="courseNumber"
        />
        <Field
          name="description"
          label="description"
        />
        <Field
          name="creditHours"
          label="creditHours"
        />
      </Fields>
      <CreateForm
        title="Course Creation"
        message="Create a new course!"
        trigger="Create course"
        onSubmit={task => courseService.create(task)}
        submitText="Create"
        validate={(values) => {
          const errors = {};
 
          return errors;
        }}
      />
 
      <UpdateForm
        title="Course Update Process"
        message="Update course"
        trigger="Update"
        onSubmit={task => courseService.update(task)}
        submitText="Update"
        validate={(values) => {
          const errors = {};
 
          return errors;
        }}
      />
 
      <DeleteForm
        title="Course Delete Process"
        message="Are you sure you want to delete the course?"
        trigger="Delete"
        onSubmit={task => courseService.delete(task)}
        submitText="Delete"
        validate={(values) => {
          const errors = {};
          
          return errors;
        }}
      />
    </CRUDTable>
  </div>
);

CourseTable.propTypes = {};

export default CourseTable;
