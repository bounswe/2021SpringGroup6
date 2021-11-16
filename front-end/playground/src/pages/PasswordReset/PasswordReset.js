import React from "react"
import './PasswordReset.css';
import Form from "react-bootstrap/Form"
import Button from "react-bootstrap/Button"
import Card from "react-bootstrap/Card"
import FormControl from "react-bootstrap/FormControl"
import Alert from "react-bootstrap/Alert"
import axios from 'axios';

const baseURL = "/users/recover";

class PasswordReset extends React.Component {

    constructor() {
        super()
        this.state = {
            status: false,
            form: {email: ""}, 
            isProblematic: false
        }


        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);

    }


    handleChange(event) {

        if (event.target.name === "email") {
            let fieldName = event.target.name;
            let fleldVal = event.target.value;
            this.setState({form: {...this.state.form, [fieldName]: fleldVal}})
            console.log(this.state.form.email)
        } else {
            console.log(event.target.checked)
            this.setState({
                [event.target.id]: event.target.checked
              });
            console.log(this.state.status)
        }
        
    }

    handleSubmit(event) {
        event.preventDefault();


        if(this.state.form.email === "") {
            alert('Not a valid email')
        }
        else if (! this.state.form.email.includes("@")) {
            alert('Not a valid email')
        }
        else if (this.state.status === false) {
            alert('Checkme forgotten')
        } else {
            
            
            console.log('Reached1')
            axios
            .post(baseURL, {
                email : "elif@example.com",
                password : "12fgh45y2",
                identifier : "elif",
                name : "elif",
                surname : "ball",
                location : "trabzon",
                age : 22,
                gender : "female",
                sports : [{"sport":"soccer", "skill_level":2}]
            }).then((response) => {
                if(response.status === 200 || response.status === 201) {
                    alert('If email provided is correct, a reset password is sent, please check spam.')
                } else {
                    alert('Not a valid email')
                }
            }
            ).catch((error) => {
                alert('There is an error. Try again later')
            })
            console.log('Reached2')
            
        }
    }


    render() {
        return (
            <div className='resetpage'>

                {/* From https://react-bootstrap.netlify.app/components/forms/*/}
                <Card variant="success" style={{ margin: '40px'}} className='all' >
                    <h1 className="forgot-title" style={{ fontSize: '50px'}}>Password Reset Page</h1>   
                    
                    <Form className="forgot-informationForm"onSubmit={this.handleSubmit} >
                        <Form.Group className="mb-3" controlId="email">
                            <Form.Label style={{ fontSize: '30px'}}>Email</Form.Label>
                            {/*<Form.Control placeholder="Enter email" />*/}
                            
                            <FormControl 
                                type='text'
                                name='email' 
                                placeholder='Enter email' 
                                defaultValue={this.state.form.email}
                                onChange={this.handleChange.bind(this)}
                            />   
                        </Form.Group>
                        <Form.Group className="mb-3" controlId="status">
                            {/*<Form.Check type="checkbox" label="Check me out" />*/}
                            <Form.Check
                                type="checkbox" 
                                label="Check me out"
                                checked={this.state.status}
                                onChange={this.handleChange}                    
                            />
                        </Form.Group>
                        <br /><br />
                        <Button variant="primary" type="submit">
                            Submit
                        </Button>
                        
                    </Form>
                </Card>
            </div>
        )
    }

}

export default PasswordReset







