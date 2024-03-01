import React from 'react';
import { Container, Row, Col } from 'flowbite';

function MyLayout() {
  return (
    <Container>
      <Row>
        <Col size="6">
          Left Side
        </Col>
        <Col size="6">
          Right Side
        </Col>
      </Row>
    </Container>
  );
}

export default MyLayout;
