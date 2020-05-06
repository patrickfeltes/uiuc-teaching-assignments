import React, { Component } from 'react';
import Select from 'react-select';
import ButtonLoader from './ButtonLoader';
const JsonTable = require('ts-react-json-table');
const BASE_URL = 'https://cs411-server.herokuapp.com';

export default class RecommendationPage extends Component {

    constructor(props) {
        super(props);

        this.state = {
            options: null,
            attributes: null,
            taughtCourses: null,
            relatedInstructors: null,
            recommendedCourses: null,
        };
    }

    handleChange = (newValue) => {
        const instructorID = newValue["value"];

        fetch(BASE_URL + '/course?instructor_id=' + instructorID).then(response => {
            response.json().then(data => {
                this.setState({ taughtCourses: data });
            });
        });

        fetch(BASE_URL + '/related_instructor?instructor_id=' + instructorID).then(response => {
            response.json().then(data => {
                this.setState({ relatedInstructors: data });
            });
        });

        fetch(BASE_URL + '/instructor?instructor_id=' + instructorID).then(response => {
            response.json().then(data => {
                this.setState({ attributes: data });
            });
        });

        fetch(BASE_URL + '/get_recommended_courses?instructor_id=' + instructorID).then(response => {
            response.json().then(data => {
                this.setState({ recommendedCourses: data });
            });
        });
    };

    componentWillMount() {
        fetch(BASE_URL + '/instructor').then(response => {
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
                <h1>Professor Information</h1>
                {this.state.attributes ? <JsonTable rows={this.state.attributes} /> : <div />}
                <h1>Taught Courses</h1>
                {this.state.taughtCourses ? <JsonTable rows={this.state.taughtCourses} /> : <div />}
                <h1>Recommended Courses</h1>
                {this.state.recommendedCourses ? <JsonTable rows={this.state.recommendedCourses} /> : <div />}
                <h1>Instructors who also taught these courses</h1>
                {this.state.relatedInstructors ? <JsonTable rows={this.state.relatedInstructors} /> : <div />}
            </div>
        );
    }
}
