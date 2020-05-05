import React, { Component } from 'react';
import Select from 'react-select';
import ButtonLoader from './ButtonLoader';
const JsonTable = require('ts-react-json-table');

export default class CourseSearchPage extends Component {

    constructor(props) {
        super(props);

        this.state = {
            options: null,
            attributes: null,
            professors: null,
            relatedCourses: null
        };
    }

    handleChange = (newValue) => {
        const courseID = newValue["value"];

        fetch('/get_instructors_who_taught_this_course?course_id=' + courseID).then(response => {
            response.json().then(data => {
                this.setState({ professors: data });
            });
        });

        fetch('/get_courses_related_to_this_one?course_id=' + courseID).then(response => {
            response.json().then(data => {
                this.setState({ relatedCourses: data });
            });
        });

        fetch('/attributes_of_course?course_id=' + courseID).then(response => {
            response.json().then(data => {
                this.setState({ attributes: data });
            });
        });
    };

    componentWillMount() {
        fetch('/course').then(response => {
            response.json().then(data => {
                var mappedData = data.map((val) => { return { label: val["courseNumber"], value: val["courseID"]} });
                this.setState({ options: mappedData });
            });
        });
    }

    render() {
        return (
            <div className="container">
                {this.state.options ? <Select options={this.state.options} onChange={this.handleChange} /> : <div></div>}
                <h1>Course Information</h1>
                {this.state.attributes ? <JsonTable rows={this.state.attributes} /> : <div />}
                <h1>Professors who taught this course</h1>
                {this.state.professors ? <JsonTable rows={this.state.professors} /> : <div />}
                <h1>Courses also taught by these instructors</h1>
                {this.state.relatedCourses ? <JsonTable rows={this.state.relatedCourses} /> : <div />}
            </div>
        );
    }
}
