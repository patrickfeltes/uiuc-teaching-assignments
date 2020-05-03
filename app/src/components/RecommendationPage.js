import React, { Component } from 'react';
import Select from 'react-select';
const JsonTable = require('ts-react-json-table');

export default class RecommendationPage extends Component {

    constructor(props) {
        super(props);

        this.state = {
            options: null,
            jsonData: null
        };
    }

    handleChange = (newValue) => {
        const instructorID = newValue["value"];

        fetch('/instructor').then(response => {
            response.json().then(data => {
                this.setState({ jsonData: data });
            });
        });

        this.setState({ instructorID: newValue["value"] });
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
                {this.state.options ? 
                <Select options={this.state.options} onChange={this.handleChange} /> 
                : <div></div>}
                {this.state.jsonData ? <JsonTable rows={this.state.jsonData} /> : <div />}
            </div>
        );
    }
}