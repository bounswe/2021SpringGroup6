import React from "react"
import Card from "react-bootstrap/Card";
import './Footer.css';

function Footer() {
    return(
        <div>


            <Card bg="danger" className="footer">
                <Card.Header  >Contact Information</Card.Header>
                <Card.Body>
                    <blockquote className="blockquote mb-0">
                    <p>
                        {' '}
                        Phone: 0 212 111 11 11  |    
                        email: project@gmail.com |
                        Istanbul / Turkey
                        {' '}
                    </p>
                    </blockquote>
                </Card.Body>
            </Card>

        </div>
    )
}

export default Footer