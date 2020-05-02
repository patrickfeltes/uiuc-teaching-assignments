import React, { Component } from 'react';
import AsyncSelect from 'react-select';
import Select from 'react-select';

// const loadOptions = (inputValue, callback) => {
//     fetch('/instructor').then(response => {
//         console.log(response);
//         var instructors = response.json();
//         console.log(instructors);
//         var mappedInstructors = instructors.map((value) => JSON.parse('{ "value": value["name"], label: value["instructorID"] }'));
//         console.log(mappedInstructors);
//         callback(mappedInstructors);
//     });
// };

const loadOptions2 = (inputValue, callback) => {
    setTimeout(callback([{ label: "label", value: 1}]), 1000);
};

const options = [{ label: "label", value: 1}];

export default class RecommendationPage extends Component {

    constructor(props) {
        super(props);

        this.state = {
            options: null
        };
    }

    componentWillMount() {
        fetch('/instructor').then(response => {
            response.json().then(data => {
                console.log(data);
                var mappedData = data.map((val) => { return { label: val["name"], value: val["instructorID"]} });
                this.setState({ options: mappedData });
            });
        });
    }

    render() {
        console.log("render")
        return (
            <div className="container">
            {this.state.options ? <Select options={this.state.options} /> : <div></div>}
            </div>
        );
    }
}