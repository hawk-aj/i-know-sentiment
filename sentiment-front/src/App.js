import './App.css';
import Form from './components/Form';

import { useEffect,useState } from 'react';

function App() {
const [sentiment, setSentiment] = useState([]);
const [inputText, setInputText] = useState(' ');

// const sentence = 'that was amazing';
useEffect(() => {
  fetch("/query-sentiment?reqstring="+inputText).then(response => 
  response.json().then(data => setSentiment(data.response))
  );
});

return(
<div className='App'>
<div className="inner-div">
<Form setSentiment = {setSentiment} setInputText = {setInputText} inputText = {inputText} />
<br></br>
You said: {inputText} <br></br>
Model says: {sentiment}
</div>
</div>);

};


export default App;
