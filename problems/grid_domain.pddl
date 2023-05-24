(define (domain grid_domain)
    (:requirements:strips :action-costs :fluents)
    (:predicates (at ?x) (adj ?x ?y) (f ?x))
  
  (:functions
    (distance ?from ?to)
    (total-cost)
    (total-step)
   )
    (:action move
        :parameters (?from ?to)
        :precondition (and(at ?from)(adj ?from ?to)(f ?to))
        :effect (and(not(at ?from))(at ?to)(increase (total-cost) (distance ?from ?to))(increase (total-step) 1))
    )
)