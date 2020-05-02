import React from 'react';
import InstructorTable from './components/InstructorTable'
import AssignmentTable from './components/AssignmentTable'
import CourseTable from './components/CourseTable'
import RelatedInstructorTable from './components/RelatedInstructorTable';
import Tabs from './components/Tabs';

import './index.css'
import RecommendationPage from './components/RecommendationPage';

const App = () => (
  <div>
    <Tabs>
      <div label="Instructors">
        <InstructorTable />
      </div>

      <div label="Courses">
        <CourseTable />
      </div>

      <div label="Recommendation">
        <RecommendationPage />
      </div>
    </Tabs>
  </div>
);
 
App.propTypes = {};
 
export default App;
