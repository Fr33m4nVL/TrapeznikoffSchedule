import React, { Component } from 'react';
import './App.css';

const homeworkItems = [
  {
    "id": 1,
    "title": "numbers 43, 42, 45, ,65 ,76, 32",
    "description": "You need do all these numbers but only even numbers",
    "subject": 3
  },
  {
      "id": 2,
      "title": "Write an essay",
      "description": "You need to write an essay on the topic\" How have I been spend my summer\"",
      "subject": 1
  },
  {
      "id": 3,
      "title": "Nothing interesting",
      "description": "Rename your name",
      "subject": 6
  }
]

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      viewCompleted: false,
      homeworkList: homeworkItems
    }
  }

  displayCompleted = status => {
    if (status) {
      return this.setState({ viewCompleted: true });
    }
    return this.setState({ viewCompleted: false });
  };

  renderTabList = () => {
    return (
      <div className="max-w-xl rounded-md shadow-md mb-12">
        <span onClick={() => this.displayCompleted(true)} className={this.state.viewCompleted ? "active" : ""}>
          complete
        </span>
        <span onClick={() => this.displayCompleted(false)} className={this.state.viewCompleted ? "" : "active"}>
          Incomplete
        </span>
      </div>
    );
  };

  renderItems = () => {
    const { viewCompleted } = this.state;
    const newItems = this.state.homeworkList.filter(item => item.completed == viewCompleted);

    return newItems.map(item => (
      <li key={item.id} className="m-6 bg-green-200 rounded-md text-center px-4">
      <span className={`homework-title mr-2 ${this.state.viewCompleted ? "completed-homework" : ""}`}></span>
      </li>
    ))
  }
  
}

export default App;
