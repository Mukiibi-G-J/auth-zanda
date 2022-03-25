import { Button } from "@material-ui/core";
import React from "react";
import { Link } from "react-router-dom";

function Home() {
  return (
    <div>
      <Button variant="contained" color="default">
        <Link to="/login">login</Link>
      </Button>
      <Button variant="contained" color="default">
        <Link to="/signup">SignIn</Link>
      </Button>
      HElloo this is the home page
    </div>
  );
}

export default Home;
