import React from 'react';
import InstructorTable from './components/InstructorTable'
import AssignmentTable from './components/AssignmentTable'
import CourseTable from './components/CourseTable'

import './index.css'

const App = () => (
  <div>
    <InstructorTable />
    <AssignmentTable />
    <CourseTable />
  </div>
);
 
App.propTypes = {};
 
export default App;
