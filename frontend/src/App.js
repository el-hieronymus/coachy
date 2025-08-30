import { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [sections, setSections] = useState([]);

  useEffect(() => {
    const slugs = ['speaker-coaching', 'sales-enablement', 'technical-sales'];
    Promise.all(
      slugs.map(slug =>
        fetch(`/api/${slug}/`).then(res => res.json().then(data => ({ slug, ...data })))
      )
    ).then(setSections);
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Coachy Services</h1>
      </header>
      {sections.map(sec => (
        <section key={sec.slug} className="Service-section">
          <h2>{sec.title}</h2>
          <p>{sec.body}</p>
        </section>
      ))}
    </div>
  );
}

export default App;
