import React from "react";
import { useState,useEffect } from "react";

const Form = ({setSentiment, setInputText, inputText}) => {
// here we can write js functions for the different actions
  const [tempText, updateTemp] = useState('');
  const inputTextHandler = (e) => {
    console.log(e.target.value);
    updateTemp(e.target.value);
  };

  const submitTextHandler = (e) => {
    e.preventDefault();
    setInputText(tempText);
    updateTemp('');
    // setInputText("");
  };

  return (
    <form>
        <input value={tempText} onChange = {inputTextHandler} type= 'text' className='todo-input'/>
        <button onClick={submitTextHandler} className='todo-button' type='submit'>
          Submit
        </button>
    </form>
  );
}

export default Form