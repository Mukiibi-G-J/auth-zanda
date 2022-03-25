import logo from "./logo.svg";
import "./App.css";
import SignUp from "./components/Register";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import SignIn from "./components/Login";
import Home from "./components/Home";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/signup" element={<SignUp />} />
          <Route path="/login" element={<SignIn />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
