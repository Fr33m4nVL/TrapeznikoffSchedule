import React, { Component } from 'react';
import axios from 'axios';
import Homework from './homework';
import Test from './test';

class SubjectTitle extends Component {
    state = {
        subjects: [],
    };

    componentDidMount() {
        this.getSubjects();
    };

    getSubjects() {
        axios
            .get('http://127.0.0.1:8000/api/v1/subjects')
            .then(res => {
                this.setState({ subjects: res.data});
            })
            .catch(err => {
                console.log(err);
            });
    };




    render() {
        const subjects = this.state.subjects
        const listSubjects = subjects.map((subject) => <h1 className="text-white text-2xl text-center py-5" key={subject.id}>{subject.name}</h1>);
        console.log(listSubjects);
        
        return(
            <div className="bg-green-500 rounded-t-lg h-20">
                {listSubjects[0]}
            </div>
        );
    };
};

class Subject extends Component {
    render() {
        let CardStyle = {
            'height': 300
        };
        
        return ( 
           <div className="bg-white ml-12 w-1/5 rounded-lg shadow-2xl" style={CardStyle}>
               <SubjectTitle />
               <Homework subjectId={this.state.subjects.filter(id=2)} />
           </div>
        );
    };
};
 
export default Subject;