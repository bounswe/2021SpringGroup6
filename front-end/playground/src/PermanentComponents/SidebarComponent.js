import {React, Fragment} from "react"
import Nav from 'react-bootstrap/Nav';
import { Link } from 'react-router-dom';
import './SidebarComponent.css';


function SidebarComponent() {
    return(
        <Fragment>
            {/* From https://stackoverflow.com/questions/60482018/make-a-sidebar-from-react-bootstrap */}
            <Nav id="sidebar" 
                className="d-md-block  sidebar"
                activeKey="/home"
                onSelect={selectedKey => alert(`selected ${selectedKey}`)}
            >
                <Nav.Item>
                    <Nav.Link><Link to="profile" style={{color: 'inherit', textDecoration: 'inherit'}}>My Profile <hr /></Link></Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link eventKey="link-1">My Events <hr /></Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link eventKey="link-2">My Badges <hr /></Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link eventKey="link-3">My Equipments <hr /></Nav.Link>
                </Nav.Item>
            </Nav>
        </Fragment>
    )
}

export default SidebarComponent