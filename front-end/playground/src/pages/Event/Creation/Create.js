import {React, useState, useEffect, useContext, useRef} from 'react';
import { Card } from 'react-bootstrap'
import './Create.css';
import {UserContext} from '../../../UserContext';
import axios from 'axios';
import SportNames from '../../../PermanentComponents/SportNames.js';
import { Button, Input, Label,  UncontrolledCollapse } from 'reactstrap';

import { Wrapper, Status } from "@googlemaps/react-wrapper";

function MyMapComponent({center, /* google.maps.LatLngLiteral */ zoom, /* number */}) {
    const size = 450;
    const ref = useRef();

    useEffect(() => {
        new window.google.maps.Map(ref.current, {center, zoom});
    });

    return <div style={{height: `${size}px`, width: `${size}px`}} sty ref={ref} id="map" />;
}

const render = (status /* Status */ ) /* ReactElement */ => {
        if (status === Status.LOADING) return <h3>{status} ..</h3>;
        if (status === Status.FAILURE) return <h3>{status} ..</h3>;
        return null;
};



function CreateEvent() {
    const center = { lat: -34.397, lng: 150.644 };
    const zoom = 4;

    return (
        <div style={{minWidth: '45%', padding: '4rem 0'}}>
            <Wrapper apiKey={"AIzaSyBM3PtscbF-rGEWmutApiLkbU2_0qHWiYE"} render={render}>
                <MyMapComponent center={center} zoom={zoom} />
            </Wrapper>
        </div>
    )
}

export default CreateEvent;
