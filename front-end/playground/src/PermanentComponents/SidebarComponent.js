import React from "react"
import Nav from 'react-bootstrap/Nav';
import './SidebarComponent.css';


function SidebarComponent() {
    return(
        <div>
            {/* From https://stackoverflow.com/questions/60482018/make-a-sidebar-from-react-bootstrap */}
            <>
                <Nav id="sidebar" className="col-md-12 d-none d-md-block bg-warning sidebar"
                activeKey="/home"
                onSelect={selectedKey => alert(`selected ${selectedKey}`)}
                >
                    <div className="sidebar-sticky"></div>
                <Nav.Item>
                    <Nav.Link href="/home">My Profile <hr /></Nav.Link>
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

            </>
        </div>
    )
}

export default SidebarComponent