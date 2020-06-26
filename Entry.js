const name = "<img src='something' onerror='alert(\"foo!\")' />";

class EntryComponent extends React.Component {
  render() {
    return <h1> Hello {name}!</h1>;
  }
  //Name will not be executed because variables are outputted as strings because of JSX!.
}
