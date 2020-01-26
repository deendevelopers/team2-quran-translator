import React from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import "./styles.css";

import SurahList from "./components/screens/SurahList";
import VerseList from "./components/screens/VerseList";
import WordPage from "./components/screens/WordPage";

export default function App() {
  return (
    <Router>
      <div className="Container">
        <Link className="HomeLink" to="/">
          Home
        </Link>

        <Switch>
          <Route path="/:verses/:verseNumber">{<WordPage />}</Route>
          <Route path="/:verses">{<VerseList />}</Route>
          <Route path="/">
            <SurahList />
          </Route>
        </Switch>
      </div>
    </Router>
  );
  // return <SurahList />;
}
