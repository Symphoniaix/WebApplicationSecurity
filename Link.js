//Running a script using the href attribute!
const linkURL = "javascript:alert('foo!');";

class Link extends React.Component {
  render() {
    return <a href={linkURL}>Click me to execute the script!</a>; //
  }
  //!IMPORTANT: not allowing keywords like "javascript" or specific characters are not sufficient as they can be decoded by attacker!.
}
