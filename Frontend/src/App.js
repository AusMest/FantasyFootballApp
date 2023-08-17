import Fetch from './components/fetch';
import Runners from './components/runners';
import {Routes,Route} from 'react-router-dom'

export default function App(){
    return(
        <div className='App'>
            <header>
            </header>
            <div id='secwrapper'>
                <section >
                
                    <Routes>
                        <Route path="/" element={<Fetch/>}/>
                        <Route path="runners" element={<Runners/>}/>
                    </Routes>
                    
                </section>
            </div>
        </div>
    )
}