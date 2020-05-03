import React, { Component } from 'react';
import Select from 'react-select';
import ButtonLoader from './ButtonLoader';
const JsonTable = require('ts-react-json-table');

export default class RecommendationPage extends Component {

    constructor(props) {
        super(props);

        this.state = {
            options: null,
            taughtCourses: null,
            relatedInstructors: null
        };
    }

    handleChange = (newValue) => {
        const instructorID = newValue["value"];

        fetch('/course?instructor_id=' + instructorID).then(response => {
            response.json().then(data => {
                this.setState({ taughtCourses: data });
            });
        });

        fetch('/related_instructor?instructor_id=' + instructorID).then(response => {
            response.json().then(data => {
                this.setState({ relatedInstructors: data });
            });
        });
    };

    componentWillMount() {
        fetch('/instructor').then(response => {
            response.json().then(data => {
                var mappedData = data.map((val) => { return { label: val["name"], value: val["instructorID"]} });
                this.setState({ options: mappedData });
            });
        });
    }

    render() {
        return (
            <div className="container">
                <ButtonLoader />
                {this.state.options ? <Select options={this.state.options} onChange={this.handleChange} /> : <div></div>}
                <h1>Taught Courses</h1>
                {this.state.taughtCourses ? <JsonTable rows={this.state.taughtCourses} /> : <div />}
                <h1>Instructors who also taught these courses</h1>
                {this.state.relatedInstructors ? <JsonTable rows={this.state.relatedInstructors} /> : <div />}
            </div>
        );
    }
}