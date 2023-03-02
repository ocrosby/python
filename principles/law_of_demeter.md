# Law of Demeter (LoD)

The Law of Demeter, also known as the principle of least knowledge, is a design guideline for developing software, particularly object-oriented programs.

* Each unit should have only limited knowledge about other units: or units "closely" related to the current unit.
* Each unit should only talk to its friends; don't talk to strangers.
* Only talk to your immediate friends.

The fundamental notion is that a given object should assume as little as possible about the structure or properties of anything else (including its subcomponents), in accordance with the principle of "information hiding". It may be viewed as a corollary to the principle of least privilege, which dictates that a module possess only the information and resources necessary for its legitimate purpose.

<dl>
    <dt><strong>Principle of Minimal Privilege</strong></dt>
    <dd>In a particular abstraction layer of a computing environment, every module (such as a process, a user, or a program, depending on the subject) must be able to access only the information and resources that are necessary for its legitimate purpose.</dd>
</dl>

In Object-Oriented programming


An object a can request a service (call a method) of an object instance b, but object a should not "reach through" object b to access yet another object, c, to request its services. Doing so would mean that object a implicitly requires greater knowledge of object b's internal structure.

Instead, b's interface should be modified if necessary so it can directly serve object a's request, propagating it to any relevant subcomponents. Alternatively, a might have a direct reference to object c and make the request directly to that. If the law is followed, only object b knows its own internal structure.

## References

* [Principle of Least Privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege)