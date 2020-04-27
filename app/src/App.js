import React from 'react';
import InstructorTable from './components/InstructorTable'
import AssignmentTable from './components/AssignmentTable'
import CourseTable from './components/CourseTable'
import RelatedInstructorTable from './components/RelatedInstructorTable';

import './index.css'

const App = () => (
  <div>
    <InstructorTable />
    <AssignmentTable />
    <CourseTable />
    <RelatedInstructorTable />
  </div>
);
 
App.propTypes = {};
 
export default App;
