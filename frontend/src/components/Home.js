import { useEffect, useState } from "react";
import axios from "axios";

export const Home = () => {
    const [message, setMessage] = useState('');

    useEffect(() => {
        if (localStorage.getItem('access_token') === null) {
            window.location.href = '/login'
        } else {
            (async () => {
                try {
                    const { data } = await axios.get(
                        'http://localhost:8000/home/', {
                            headers: {
                                'Content-Type': 'application/json',
                            }
                        }
                        , { withCredentials: true })
                    setMessage(`Welcome, ${localStorage.getItem('username')}!`);
                } catch (e) {
                    console.log('not authorized');
                }
            })()};
    }, []);

    return (
        <div className="form-signin mt-5 text-center">
            <h3> { message } </h3>
        </div>
    )
}