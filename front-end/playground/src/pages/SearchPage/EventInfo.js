import React from "react"
import { Card } from "react-bootstrap"
import { Link } from "react-router-dom";
import Button from "react-bootstrap/Button";


import './EventInfo.css'

function EventInfo(props) {
    return (
        <div class='wholeComponent'>
            <Card class='whole'>
                <Card.Body><h3 id="title">{props.name}</h3><br/><p>{props.description ? props.description : 'No description available'}</p></Card.Body>
                <Link to={"/event/" + props.id} >
                    <Button variant="info" size="lg">
                        Click to view the event
                    </Button>
                </Link>
                
            </Card>
            <br/><br/>
            {/*<h3>{props.name}</h3>
            <p>{props.description}</p>*/}
        </div>
    )
}

export default EventInfo