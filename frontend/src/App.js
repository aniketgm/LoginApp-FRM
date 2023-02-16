import './css/normalize.css';
import './css/styles.css';
import { HashRouter, Routes, Route } from "react-router-dom";
import AuthPage from './components/AuthPage';
import Dashboard from './components/Dashboard';

function App() {
  return (
    <HashRouter>
      <div className="App">
        <Routes>
          <Route path="/" exact element={<AuthPage />} />
          <Route path="/dashboard" element={<Dashboard {id, name, email} />} />
        </Routes>
      </div>
    </HashRouter>
  );
}

export default App;
