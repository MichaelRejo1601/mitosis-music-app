import {useEffect, useState, useRef} from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from './assets/vite.svg';
import './App.css';

async function addCount() {

    try {
        fetch('http://localhost:8000/plusplus')
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Server error");
                }
            })
    } catch (err) {
        console.error("Failed to increment:", err);
    }

}

function App() {
    const [count, setCount] = useState(0);
    const [message, setMessage] = useState({});

    const hasIncremented = useRef(false);

    // Fetch message from backend on mount
    useEffect(() => {
        fetch('http://localhost:8000/')
            .then(response => response.json())
            .then(data => setMessage(data));
    }, []);

    useEffect(() => {
        if (hasIncremented.current) return;
        hasIncremented.current = true;

        addCount()

    }, []);

    useEffect(() => {
        // Immediate fetch when component mounts
        const fetchCount = () => {
            fetch('http://localhost:8000/getcount')
                .then(response => response.json())
                .then(data => setCount(data.count))
                .catch(error => console.error("Error fetching count:", error));
        };

        // Run immediately on mount
        fetchCount();

        // Set interval to fetch data every 5 seconds
        const intervalId = setInterval(fetchCount, 5000); // Run every 5 seconds

        // Cleanup interval on unmount
        return () => clearInterval(intervalId);
    }, []); 

    return (
        <>
            <div>
                <a href="https://vite.dev" target="_blank">
                    <img src={viteLogo} className="logo" alt="Vite logo"/>
                </a>
                <a href="https://react.dev" target="_blank">
                    <img src={reactLogo} className="logo react" alt="React logo"/>
                </a>
            </div>
            <h1>Vite + React</h1>
            <div className="card">
                Current Visits: {count}
                <p>
                    Edit <code>src/App.jsx</code> and save to test HMR
                </p>
            </div>
            <div>
                <header>
                    <h2>Message from MongoDB via FastAPI: I &lt;3 {message.value}</h2>
                </header>
            </div>
        </>
    );
}

export default App;
