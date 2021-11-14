import {React, Fragment} from "react"
import Card from "react-bootstrap/Card";
import './Footer.css';

function Footer() {
    return(
        <Fragment>
            <div className="footer-container">
                <p>Phone: 0 212 111 11 11</p>
                <p><a href="mailto:squadgamebypluto@gmail.com">squadgamebypluto@gmail.com</a></p>
                <p>Istanbul / Turkey</p>
            </div>
            {/* <Card bg="danger" className="footer">
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
            </Card> */}
        </Fragment>
    )
}

export default Footer