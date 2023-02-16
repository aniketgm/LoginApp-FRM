import React from "react";
import { userApis } from "./Apis";
import { useLocation, useNavigate } from "react-router-dom";

const Dashboard = () => {

  let navigate = useNavigate()

  // Capture the state set by navigate call from AuthPage
  let location = useLocation()
  const { _id, name, email } = location.state;

  async function handleLogout() {
    const headers = {
      // Setting content-type as plain text avoids OPTIONS call.
      'Content-Type': 'text/plain',
    }
    const api = userApis.userLogout
    let resp = await fetch(api.url, {
      method: api.method,
      headers: headers,
      body: {}
    });
    if (resp.ok) {
      navigate('/')
    } else {
      throw Error(resp.status)
    }
  }

  return (
    <div className="card-wrapper">
      <div className="card">
        <h1 className="center">Dashboard</h1>
        <p className="center">You are currently logged in.</p>
        <div className="center">
          <button className="btn btn--secondary" onClick={handleLogout}>Log Out</button>
        </div>
      </div>

      <div className="card">
        <h2 className="center">Your Info</h2>
        <p>
          <strong>ID:</strong> {_id ? _id : ""}<br />
          <strong>Name:</strong> {name ? name : ""}<br />
          <strong>Email:</strong> {email ? email : ""}
        </p>
      </div>
    </div>
  )
}

export default Dashboard
