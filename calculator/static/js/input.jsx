import React from 'react';
import PropTypes from 'prop-types';


class Input extends React.Component {
    constructor(props) {
        // Initialize mutable state
        super(props);
        this.state = {
            text = '',
            selected = '',
        };
    }

    componentdidMount() {
        const {
            text,
        } = this.props;
        const text = text;
        const select = window.getSelection();
        this.setState({
            text: text,
            selected: select,
        })
    }

    render() {
        const { text, selected } = this.state;
        if(selected.length > 0) {
            return (
                <div>
                    <input type="text" name = "inp"/>
                </div>
            )
        }
    }
}

const domContainer = document.querySelector('#reactEntry');
ReactDOM.render(e(Input), domContainer);

export default Input;