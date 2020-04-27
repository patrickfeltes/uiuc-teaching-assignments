import React from "react";
import CRUDTable,
{
  Fields,
  Field,
  CreateForm,
  UpdateForm,
  DeleteForm,
} from 'react-crud-table';
 
const relatedInstructorService = {
  fetchItems: (payload) => {
    return fetch('/related_instructor').then(response => {
      return response.json();
    });
  },
  create: (assignment) => {
    return fetch('/related_instructor', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(assignment)
    });
  },
  update: (assignment) => {
    return fetch('/related_instructor', {
      method: 'PUT',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(assignment)
    });
  },
  delete: (data) => {
    return fetch('/related_instructor/' + data.relatedID, {
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
 
const RelatedInstructorTable = () => (
  <div style={styles.container}>
    <CRUDTable
      caption="related instructors"
      fetchItems={payload => relatedInstructorService.fetchItems(payload)}
    >
      <Fields>
        <Field
          name="relatedID"
          label="relatedInstructorTable"
          hideInCreateForm
          hideInUpdateForm
        />
        <Field
          name="relatedInstructorID1"
          label="relatedInstructorID1"
        />
        <Field
          name="relatedInstructorID2"
          label="relatedInstructorID2"
        />
      </Fields>
      <CreateForm
        title="Related Instructor Creation"
        message="Create a new instructor relation!"
        trigger="Create relation"
        onSubmit={task => relatedInstructorService.create(task)}
        submitText="Create"
        validate={(values) => {
          const errors = {};
 
          return errors;
        }}
      />
 
      <UpdateForm
        title="Instructor relation Update Process"
        message="Update instructor relation"
        trigger="Update"
        onSubmit={task => relatedInstructorService.update(task)}
        submitText="Update"
        validate={(values) => {
          const errors = {};
 
          return errors;
        }}
      />
 
      <DeleteForm
        title="Instructor Relation Delete Process"
        message="Are you sure you want to delete the assignment?"
        trigger="Delete"
        onSubmit={task => relatedInstructorService.delete(task)}
        submitText="Delete"
        validate={(values) => {
          const errors = {};
          
          return errors;
        }}
      />
    </CRUDTable>
  </div>
);

RelatedInstructorTable.propTypes = {};

export default RelatedInstructorTable;
