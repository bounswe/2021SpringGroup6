import React from "react"
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Container from 'react-bootstrap/Container';



function Header() {
    return (
       <div>
           {/* From https://react-bootstrap.github.io/components/navbar/ */}
           <Navbar className="header" bg="info" expand="lg">
                <Container>
                    <Navbar.Brand href="#home">Project Name</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <Nav.Link href="#home">Home</Nav.Link>
                        <Nav.Link href="#link">Events</Nav.Link>
                        <NavDropdown title="Additional Features" id="basic-nav-dropdown">
                        <NavDropdown.Item href="#action/3.1">Equipments</NavDropdown.Item>
                        <NavDropdown.Divider />
                        <NavDropdown.Item href="#action/3.2">Badges</NavDropdown.Item>
                        </NavDropdown>
                    </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
       </div>
    )
}

export default Header;