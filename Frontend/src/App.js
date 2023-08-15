import Fetch from './components/fetch';
import {Routes,Route} from 'react-router-dom'

export default function App(){
    return(
        <div className='App'>
            <header>
            </header>
            <div id='secwrapper'>
                <section>
                <Routes>
                    <Route path="/" element={<Fetch/>}/>
                </Routes>
                </section>
            </div>
        </div>
    )
}