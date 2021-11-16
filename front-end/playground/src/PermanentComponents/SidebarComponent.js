import {React, Fragment, useContext} from "react"
import Nav from 'react-bootstrap/Nav';
import { Link } from 'react-router-dom';
import './SidebarComponent.css';
import {UserContext} from '../UserContext'


function SidebarComponent() {
    const {user, setUser} = useContext(UserContext);
    return(
        <Fragment>
            {/* From https://stackoverflow.com/questions/60482018/make-a-sidebar-from-react-bootstrap */}
            <Nav id="sidebar" 
                className="d-md-block  sidebar"
                activeKey="/home"
                onSelect={selectedKey => {
                    if (selectedKey === "logout") {
                        setUser({identifier: ""})
                    } else
                        alert(`selected ${selectedKey}`)
                }}
            >
                <Nav.Item>
                    <Nav.Link>
                        <Link to="profile" style={{color: 'inherit', textDecoration: 'inherit'}}>
                            My Profile <hr />
                        </Link>
                    </Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link eventKey="Events">My Events <hr /></Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link eventKey="Badges">My Badges <hr /></Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link eventKey="Equipments">My Equipments <hr /></Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link eventKey="logout">Logout <hr /></Nav.Link>
                </Nav.Item>
            </Nav>
        </Fragment>
    )
}

export default SidebarComponent