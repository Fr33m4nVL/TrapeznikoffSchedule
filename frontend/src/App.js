import React, { Component } from 'react';
import Navbar from './components/navbar';
import Subject from './components/subject';

class App extends Component {
    render() {
        return(
            <>
                <Navbar />
                <Subject />
            </>
        );
    }
}

export default App;
