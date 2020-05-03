import React, { Component } from "react";

export default class ButtonLoader extends Component {
  state = {
    loading: false
  };

  fetchData = () => {
    this.setState({ loading: true });

    fetch('/update_similarities').then(response => {
        this.setState( { loading: false });
    });
  };

  render() {
    const { loading } = this.state;

    return (
        <button className="loading-button" onClick={this.fetchData} disabled={loading}>
            {loading && (
            <i
                className="fa fa-refresh fa-spin"
                style={{ marginRight: "5px" }}
            />
            )}
            {loading && <span>Refresh Course Similarities (If you added courses or changed descriptions).</span>}
            {!loading && <span>Refreshing Course Similarities (about 10 s)</span>}
        </button>
    );
  }
}
