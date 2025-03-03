import { useEffect, useState } from 'react';
import axios from 'axios';
import './For_CSS/style.css';  

function App() {
  const [postMessage, setPostMessage] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/v1/api/post/')
      .then(response => {
        setPostMessage(response.data); 
      })
      .catch(error => {
        console.error("Error fetching data:", error);
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1 className="header-text">Welcome to React Integration</h1>
        <p className="header-subtext">Activity 3</p>
      </header>

      <h2 className="fetch-title">All the fetched data from Django</h2>

      <div className="posts-container">
        {postMessage.length > 0 ? (
          postMessage.map((obj, index) => (
            <div className="post-card" key={index}>
              <h3><strong>Title:</strong> {obj.title}</h3>
              <p><strong>Content:</strong> {obj.content}</p>
              <span className="author">Author ID: {obj.author}</span>
            </div>
          ))
        ) : (
          <p className="loading-text">Loading posts...</p>
        )}
      </div>
    </div>
  );
}

export default App;
