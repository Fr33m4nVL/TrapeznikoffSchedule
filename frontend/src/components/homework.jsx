import React, { Component } from 'react';
import axios from 'axios';

class Homework extends Component {
    state = {
        homeworks: [],
    };

    componentDidMount() {
        this.getHomeworks();
    };
    
    getHomeworks() {
        axios
            .get('http://localhost:8000/api/v1/homeworks')
            .then(res => {
                this.setState({ homeworks : res.data });
            })
            .catch(err => {
                console.log(err);
            });
    };
    
    render() { 
        const homeworks = this.state.homeworks
        console.log(homeworks);
        return ( 
            <div>
                {this.state.homeworks.filter({subjectId})}
            </div>
        );
    };
}
 
export default Homework;