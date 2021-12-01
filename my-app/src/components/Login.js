import React, { useState, useEffect } from 'react';

const Login = () => {
  
  const [username, setUsername]= useState('')
  const [password, setPassword]= useState('')
  // const [email, setEmail] = useState('')
  const onSubmit = e => {
    e.preventDefault();

    const user = {
      username: username,
      password: password
    };

    fetch('http://127.0.0.1:8000/user/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(user)
    })
      .then(res => res.json())
      .then(data => {
        if (data.key) {
          localStorage.clear();
          localStorage.setItem('token', data.key);
          window.location.replace('http://localhost:3000/booking');
        } else {
          setUsername('');
          setPassword('');
          localStorage.clear();
          
        }
      });
  };

  return (
    <div>
      <h1>Login</h1>
     
        <form onSubmit={onSubmit}>
          <label htmlFor='name'>Name:</label> <br />
          <input
            name='name'
            type='text'
            value={username}
            required
            onChange={e => setUsername(e.target.value)}
          />{' '}
          <br />
          {/* <label htmlFor='email'>Email:</label> <br />
          <input
            name='email'
            type='email'
            value={email}
            required
            onChange={e => setEmail(e.target.value)}
          />{' '}
          <br /> */}
          <label htmlFor='password'>NRIC:</label> <br />
          <input
            name='password'
            type='password'
            value={password}
            required
            onChange={e => setPassword(e.target.value)}
          />{' '}
          <br />
          <input type='submit' value='Login' />
        </form>
      
    </div>
  );
};

export default Login;