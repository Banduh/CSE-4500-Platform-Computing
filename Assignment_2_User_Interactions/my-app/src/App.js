import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
  
 <div>
  <h1>ABOUT ME</h1>
  <p>
    By: Bryan Tran
  </p>
  <h2>Quick info</h2>
  <p>
    Hello my name is Bryan Tran I am 20 years old and Vietnamese. Currently I am studying computer information systems at CSUSB and I also work as a pharmacy technician at CVS. 
    When I'm not at school or working I really like to play games or sometimes just do nothing because I don't know what to do. The game I'm playing right now is Palworld. 
  </p>
  <h2>CSUSB</h2>
  <div className="section">
    <p>
      I'm currently a third year here at California State University of San Bernardino. I am currently majoring in computer information systerms with a concentration on administration.
      After getting my degree I am looking forward to exploring the cyber security field. It's something that has always interested me and I want to pursue it as my career. Also
      it's nice that CSUSB has a cyber security program and department.  
    </p>
  </div>
  <h2>Goals for this class</h2>
  <p>
    The reason I took this class is because it is a requirement because I needed it to fill an elective slot. Secondly I thought it was one of the more interesting class. All the other
    classes being offered just didn't seem that interesting to me. So I went with this one because it was interesting and I was curious to know what it was about. 
  </p>
  <div>
    <div className="subsection">
      <a href="https://github.com/Banduh">GitHub</a>
    </div>
    <img src="panda.jpeg" alt="panda" />
  </div>
</div>


        <img src={logo} className="App-logo" alt="logo" />
        <p>
          .
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;